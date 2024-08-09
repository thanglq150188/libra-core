# base_test.py

import pytest
from libra.models.base import OpenAIModel, ModelLabel

@pytest.fixture
def model():
    model_label = ModelLabel.GPT_3_5_TURBO
    model_config_dict = {}
    return OpenAIModel(model_label, model_config_dict)

def test_run_method(model):
    messages = [{'content': 'Hello'}]
    result = model.run(messages=messages)
    assert isinstance(result, dict)

def test_run_method_with_invalid_model_label(model):
    model.model_label = 'invalid_label'
    with pytest.raises(ValueError):
        model.run(messages=[{'content': 'Hello'}])

def test_run_method_without_messages(model):
    with pytest.raises(TypeError):
        model.run()