#  Copyright (C) 2026. Hao Zheng
#  All rights reserved.

import unittest
from typing import get_args, get_type_hints

from openlrc.config import TranslationConfig


class TestTranslationConfigAnnotations(unittest.TestCase):
    def test_annotations_remain_serialization_friendly(self):
        hints = get_type_hints(TranslationConfig)

        self.assertIs(hints["chatbot_model"], str)
        self.assertEqual(set(get_args(hints["retry_model"])), {str, type(None)})
        self.assertEqual(set(get_args(hints["glossary"])), {str, type(None)})
