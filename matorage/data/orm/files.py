# Copyright 2020-present Tae Hwan Jung
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

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint

from matorage.data.orm.bucket import Bucket

Base = declarative_base()

class Files(Base):
    __tablename__ = 'files'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    bucket_id = Column(String(255))

    ForeignKeyConstraint(
        [bucket_id], [Bucket.id],
        name="bucket_id"
    )

    def __repr__(self):
        return "<Files(" \
                   "id='%d', " \
                   "name='%s'" \
                   "bucket_id='%s'" \
               ")>" % (
            self.id, self.name, self.bucket_id
        )