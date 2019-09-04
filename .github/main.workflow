workflow "Publish Gateway" {
  resolves = ["publish-gateway-to-pypi"]
  on = "release"
}

action "publish-gateway-to-pypi" {
  uses = "mariamrf/py-package-publish-action@master"
  secrets = ["TWINE_PASSWORD", "TWINE_USERNAME"]
  env = {
    BRANCH = "master"
    PYTHON_VERSION = "3.7.0"
    SUBDIR = "gateway-package"
  }
  needs = ["Master"]
}

# Filter for master branch
action "Master" {
  uses = "actions/bin/filter@master"
  args = "branch master"
}
