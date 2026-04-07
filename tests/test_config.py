#  Copyright (C) 2026. Hao Zheng
#  All rights reserved.

import unittest
from pathlib import Path
from typing import get_args, get_type_hints

from openlrc.config import TranslationConfig
from openlrc.models import ModelConfig


class TestTranslationConfigAnnotations(unittest.TestCase):
    def test_annotations_match_supported_runtime_inputs(self):
        hints = get_type_hints(TranslationConfig)

        self.assertIn(ModelConfig, get_args(hints["chatbot_model"]))
        self.assertIn(ModelConfig, get_args(hints["retry_model"]))

        glossary_args = set(get_args(hints["glossary"]))
        self.assertTrue({dict, str, Path, type(None)} <= glossary_args)
