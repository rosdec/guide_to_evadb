# coding=utf-8
# Copyright 2018-2023 EvaDB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pandas as pd

from evadb.catalog.catalog_type import NdArrayType
from evadb.functions.abstract.abstract_function import AbstractFunction
from evadb.functions.decorators.decorators import forward, setup
from evadb.functions.decorators.io_descriptors.data_types import PandasDataframe

from textblob import TextBlob


class SentimentAnalysis(AbstractFunction):
    """
    Arguments:
        none
    """

    @property
    def name(self) -> str:
        return "SentimentAnalysis"

    @setup(cacheable=True, function_type="object_detection", batchable=False)
    def setup(self):
        print("Setup")

    @forward(
        input_signatures=[
            PandasDataframe(
                columns=["twit"],
                column_types=[
                    NdArrayType.STR,
                ],
                column_shapes=[(1,)],
            )
        ],
        output_signatures=[
            PandasDataframe(
                columns=["label"],
                column_types=[
                    NdArrayType.STR,
                ],
                column_shapes=[(1,)],
            )
        ],
    )
    def forward(self, frames):
        tb = [TextBlob(x).sentiment.polarity for x in frames['twit']]

        df = pd.DataFrame(data=tb, columns=['label'])

        return df
