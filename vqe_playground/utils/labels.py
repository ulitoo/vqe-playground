#
# Copyright 2019 the original author or authors.
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
#


def comp_graph_node_labels(num_nodes):
    """Construct dict containing node labels beginning with A"""
    return {x: chr(x + 65) for x in range(num_nodes)}


def graph_node_labels_reversed_str(num_nodes):
    labels_dict = comp_graph_node_labels(num_nodes)
    return "".join(reversed(list(labels_dict.values())))
