#!/bin/bash

set -e

scritp_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${scritp_dir}"

poetry run pytest -s --lg-env "${scritp_dir}/labgrid-env.yaml" --lg-colored-steps -vv
