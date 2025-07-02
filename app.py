from fastapi import FastAPI
from fastapi.responses import HTMLResponse # Opcional, para servir o index.html na raiz
from fastapi.middleware.cors import CORSMiddleware # Certifique-se de que esta linha está aqui
from database import engine, Base
from routers.alunos import alunos_router
from routers.cursos import cursos_router
from routers.matriculas import matriculas_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestão Escolar", 
    description="""
        Esta API fornece endpoints para gerenciar alunos, cursos e turmas, em uma instituição de ensino.  
        
        Permite realizar diferentes operações em cada uma dessas entidades.
    """, 
    version="1.0.0",
)

# ---
# Configuração do CORS
# ---
origins = [
    "http://localhost", # Opcional: Se seu frontend estiver na mesma máquina em alguma porta default
    "http://localhost:8080", # **Essencial:** Adicione a URL completa do seu frontend React aqui (porta padrão do Create React App)    
    # Você pode adicionar outras origens se o seu frontend estiver hospedado em outro lugar
    # Por exemplo: "https://seu-dominio-frontend.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Lista de origens permitidas
    allow_credentials=True,         # Permite o envio de cookies de credenciais
    allow_methods=["*"],            # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],            # Permite todos os cabeçalhos HTTP
)
# ---

app.include_router(alunos_router, tags=["alunos"])
app.include_router(cursos_router, tags=["cursos"])
app.include_router(matriculas_router, tags=["matriculas"])

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content, media_type="text/html; charset=utf-8")