from setuptools import setup, find_packages


setup(
  name="tenant",
  version="0.0.1",
  packages=find_packages("src"),
  package_dir={"":"src"},
  entry_points={
    "console_scripts": "tenant = octoflow.tenants.tenant.cli:main",
    "octoflow.tenants": "tenant = octoflow.tenants.tenant.settings:TenantSettings"
  },
  py_modules=['settings']
)