import json
import re
from abc import ABC, abstractmethod
from copy import deepcopy
from hashlib import md5
from io import BytesIO
from typing import Any, Dict, List, Optional


class File(ABC):
    r"""Represents an uploaded file comprised of Documents"""

    def __init__(
        self,
        name: str,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        docs: Optional[List[Dict[str, Any]]] = None,
    ):
        r"""

        Args:
            name (str): The name of the file.
            id (str): The unique identifier of the file.
            metadata (Dict[str, Any], optional): Additional metadata
                associated with the file. Defaults to None.
            docs (List[Dict[str, Any]], optional): A list of documents
                contained within the file. Defaults to None.
        """
        self.name = name
        self.id = id
        self.metadata = metadata or {}
        self.docs = docs or []

    @classmethod
    @abstractmethod
    def from_bytes(cls, file: BytesIO) -> "File":
        r"""Creates a File object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                file.

        Returns:
            File: A File object.
        """

    def __repr__(self) -> str:
        return (
            f"File(name={self.name}, id={self.id}, "
            f"metadata={self.metadata}, docs={self.docs})"
        )

    def __str__(self) -> str:
        return (
            f"File(name={self.name}, id={self.id}, metadata={self.metadata})"
        )

    def copy(self) -> "File":
        r"""Create a deep copy of this File"""

        return self.__class__(
            name=self.name,
            id=self.id,
            metadata=deepcopy(self.metadata),
            docs=deepcopy(self.docs),
        )


def strip_consecutive_newlines(text: str) -> str:
    r"""Strips consecutive newlines from a string.

    Args:
        text (str): The string to strip.

    Returns:
        str: The string with consecutive newlines stripped.
    """
    return re.sub(r"\s*\n\s*", "\n", text)


class DocxFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO) -> "DocxFile":
        r"""Creates a DocxFile object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                docx file.

        Returns:
            DocxFile: A DocxFile object.
        """
        import docx2txt
        text = docx2txt.process(file)
        text = strip_consecutive_newlines(text)
        # Create a dictionary with the extracted text
        doc = {"page_content": text.strip()}
        # Calculate a unique identifier for the file
        file_id = md5(file.getvalue()).hexdigest()
        # Reset the file pointer to the beginning
        file.seek(0)
        return cls(name=file.name, id=file_id, docs=[doc])


class PdfFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO) -> "PdfFile":
        r"""Creates a PdfFile object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                pdf file.

        Returns:
            PdfFile: A PdfFile object.
        """
        # Use fitz to extract text from pdf files
        try:
            import fitz
        except ImportError:
            raise ImportError(
                "Please install `PyMuPDF` first. "
                "You can install it by running "
                "`pip install PyMuPDF`."
            )
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        docs = []
        for i, page in enumerate(pdf): # type: ignore
            text = page.get_text(sort=True)
            text = strip_consecutive_newlines(text)
            # Create a dictionary with the extracted text
            doc = {"page_content": text.strip(), "page": i + 1}
            docs.append(doc)
        # Calculate a unique identifier for the file
        file_id = md5(file.getvalue()).hexdigest()
        # Reset the file pointer to the beginning
        file.seek(0)
        return cls(name=file.name, id=file_id, docs=docs)


class TxtFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO) -> "TxtFile":
        r"""Creates a TxtFile object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                txt file.

        Returns:
            TxtFile: A TxtFile object.
        """
        # Read the text from the file
        text = file.read().decode("utf-8")
        text = strip_consecutive_newlines(text)
        # Create a dictionary with the extracted text
        doc = {"page_content": text.strip()}
        # Calculate a unique identifier for the file
        file_id = md5(file.getvalue()).hexdigest()
        # Reset the file pointer to the beginning
        file.seek(0)
        return cls(name=file.name, id=file_id, docs=[doc])

class CsvFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO) -> "CsvFile":
        r"""Creates a CsvFile object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                csv file.

        Returns:
            CsvFile: A CsvFile object.
        """
        # Parse the CSV data from the file        
        docs = []
        
        import pandas as pd
        
        df = pd.read_csv(file)
        # df = df.dropna()
        
        for i, row in df.iterrows():
            doc = {
                'page_content': row.to_json(),
            }
            docs.append(doc)
            
        # Calculate a unique identifier for the file
        file_id = md5(file.getvalue()).hexdigest()
        # Reset the file pointer to the beginning
        file.seek(0)
        return cls(name=file.name, id=file_id, docs=docs)

class JsonFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO) -> "JsonFile":
        r"""Creates a JsonFile object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                json file.

        Returns:
            JsonFile: A JsonFile object.
        """
        # Parse the JSON data from the file
        data = json.load(file)
        
        docs = []
        for i in range(len(data)):
            content = json.dumps(data[i])
            doc = {"page_content": content.strip(), "page": i + 1}
            docs.append(doc)
            
        # Calculate a unique identifier for the file
        file_id = md5(file.getvalue()).hexdigest()
        # Reset the file pointer to the beginning
        file.seek(0)
        return cls(name=file.name, id=file_id, docs=docs)


class HtmlFile(File):
    @classmethod
    def from_bytes(cls, file: BytesIO) -> "HtmlFile":
        r"""Creates a HtmlFile object from a BytesIO object.

        Args:
            file (BytesIO): A BytesIO object representing the contents of the
                html file.

        Returns:
            HtmlFile: A HtmlFile object.
        """
        # Parse the HTML data from the file
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            raise ImportError(
                "Please install `beautifulsoup4` first. "
                "You can install it by running "
                "`pip install beautifulsoup4`."
            )
        soup = BeautifulSoup(file, "html.parser")
        text = soup.get_text()
        text = strip_consecutive_newlines(text)
        # Create a dictionary with the parsed data
        doc = {"page_content": text.strip()}
        # Calculate a unique identifier for the file
        file_id = md5(file.getvalue()).hexdigest()
        # Reset the file pointer to the beginning
        file.seek(0)
        return cls(name=file.name, id=file_id, docs=[doc])


def read_file(file: BytesIO) -> File:
    r"""Reads an uploaded file and returns a File object.

    Args:
        file (BytesIO): A BytesIO object representing the contents of the file.

    Returns:
        File: A File object.
    """
    # Determine the file type based on the file extension
    if file.name.lower().endswith(".docx"):
        return DocxFile.from_bytes(file)
    elif file.name.lower().endswith(".pdf"):
        return PdfFile.from_bytes(file)
    elif file.name.lower().endswith(".txt"):
        return TxtFile.from_bytes(file)
    elif file.name.lower().endswith(".json"):
        return JsonFile.from_bytes(file)
    elif file.name.lower().endswith(".html"):
        return HtmlFile.from_bytes(file)
    elif file.name.lower().endswith(".csv"):
        return CsvFile.from_bytes(file)
    else:
        raise NotImplementedError(
            f"File type {file.name.split('.')[-1]} not supported"
        )
