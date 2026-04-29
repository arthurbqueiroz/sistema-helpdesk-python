import psycopg2
from psycopg2 import Error

# Configurações do banco de dados local
DB_CONFIG = {
    'user': 'postgres',      # Substitua pelo seu usuário do Postgres
    'password': 'sua_senha', # Substitua pela sua senha
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'helpdesk'
}

def conectar():
    """Cria a conexão com o banco de dados Postgres."""
    try:
        conexao = psycopg2.connect(**DB_CONFIG)
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

def abrir_chamado(titulo, descricao, usuario_id):
    """Insere um novo chamado no banco de dados de forma segura."""
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Uso de %s protege contra SQL Injection
            query = """INSERT INTO chamados (titulo, descricao, usuario_id) 
                       VALUES (%s, %s, %s)"""
            valores = (titulo, descricao, usuario_id)
            
            cursor.execute(query, valores)
            conexao.commit()
            print("\n✅ Chamado aberto com sucesso!")
        except Error as e:
            print(f"Erro ao inserir chamado: {e}")
        finally:
            cursor.close()
            conexao.close()

def listar_chamados_abertos():
    """Busca no banco todos os chamados com status 'Aberto'."""
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = """SELECT c.id, c.titulo, u.nome, c.data_abertura 
                       FROM chamados c
                       JOIN usuarios u ON c.usuario_id = u.id
                       WHERE c.status = 'Aberto'"""
            cursor.execute(query)
            registros = cursor.fetchall()
            
            print("\n--- Chamados Abertos ---")
            for linha in registros:
                print(f"ID: {linha[0]} | Título: {linha[1]} | Usuário: {linha[2]} | Data: {linha[3].strftime('%d/%m/%Y %H:%M')}")
            print("------------------------")
        except Error as e:
            print(f"Erro ao buscar chamados: {e}")
        finally:
            cursor.close()
            conexao.close()

def fechar_chamado(chamado_id):
    """Atualiza o status de um chamado para 'Concluído'."""
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = "UPDATE chamados SET status = 'Concluído' WHERE id = %s"
            cursor.execute(query, (chamado_id,))
            conexao.commit()
            print(f"\n✅ Chamado {chamado_id} fechado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar chamado: {e}")
        finally:
            cursor.close()
            conexao.close()