#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 1999-2020 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from .core import HasKey, HasData
# noinspection PyUnresolvedReferences
from .core import serializes, deserializes, ProviderType, Provider

_ENABLE_NEW_SERIALIZATION = os.environ.get('enable_new_serialization', '0') == '1'
if _ENABLE_NEW_SERIALIZATION:
    # noinspection PyUnresolvedReferences
    from ..serialization.serializables import FieldTypes as ValueType, \
        SerializableMeta as SerializableMetaclass, Serializable as AttributeAsDict
    # noinspection PyUnresolvedReferences
    from ..serialization.serializables import Serializable, \
        AnyField, IdentityField, BoolField, Int8Field, Int16Field, Int32Field, Int64Field, \
        UInt8Field, UInt16Field, UInt32Field, UInt64Field, Float16Field, Float32Field, Float64Field, \
        StringField, BytesField, KeyField, NDArrayField, DataTypeField, \
        SliceField, IndexField, SeriesField, DataFrameField, ListField, TupleField, DictField, \
        FunctionField, TZInfoField, IntervalArrayField, ReferenceField, OneOfField
else:
    # noinspection PyUnresolvedReferences
    from .core import ValueType, Serializable, SerializableMetaclass, AttributeAsDict, \
        AnyField, IdentityField, BoolField, Int8Field, Int16Field, Int32Field, Int64Field, \
        UInt8Field, UInt16Field, UInt32Field, UInt64Field, Float16Field, Float32Field, Float64Field, \
        StringField, BytesField, UnicodeField, KeyField, NDArrayField, DataTypeField, \
        SliceField, IndexField, SeriesField, DataFrameField, ListField, TupleField, DictField, \
        FunctionField, TZInfoField, IntervalArrayField, ReferenceField, OneOfField
from .jsonserializer import JsonSerializeProvider
try:
    from .pbserializer import ProtobufSerializeProvider
except ImportError:  # pragma: no cover
    # ProtobufSerializeProvider used in distributed environment
    pass
