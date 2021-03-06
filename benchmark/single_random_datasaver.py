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

import time
import numpy as np
from tqdm import tqdm

from matorage import DataSaver, DataConfig, DataAttribute


def preprocessing_work():
    # abstract preprocessing work
    time.sleep(1)


if __name__ == "__main__":

    data_config = DataConfig(
        endpoint="127.0.0.1:9000",
        access_key="minio",
        secret_key="miniosecretkey",
        dataset_name="array_test",
        attributes=[DataAttribute("array", "uint8", (3, 224, 224)),],
    )

    data_saver = DataSaver(config=data_config)
    row = 100
    data = np.random.rand(64, 3, 224, 224,).astype("uint8")

    start = time.time()

    for _ in tqdm(range(row)):
        preprocessing_work()
        data_saver({"array": data})

    data_saver.disconnect()

    end = time.time()
    print(end - start)
