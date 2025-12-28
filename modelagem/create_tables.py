from database import engine
from models.base import Base

import models.cliente
import models.proprietario
import models.imovel
import models.corretor
import models.contrato

Base.metadata.create_all(bind=engine)
