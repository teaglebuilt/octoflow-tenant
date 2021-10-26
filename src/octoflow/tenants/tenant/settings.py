import attr
from pathlib import Path
from airflow.models.dagbag import DagBag
from fastapi.routing import APIRouter
from octoflow.tenants.tenant.router import routes


project_path = Path(__file__).expanduser().resolve().parent


@attr.s(auto_attribs=True)
class TenantSettings:
    routes: APIRouter = routes
    dagbag: DagBag = DagBag(project_path / "dags")