# ======================================
 #   MI JARVIS — Servidor Web ☁️
 # ======================================
 from flask import Flask
 app = Flask(__name__)
 @app.route('/')
 def inicio():
     return """
     <html>
     <body style='background:#0f172a;color:#fff;font-family:sans-serif;text-align:center;padding:50px;'>
         <h1>🤖 ¡Hola Marlon!</h1>
         <h2>✅ Estoy en línea desde la nube</h2>
         <p>✨ Conectado y listo para ayudarte</p>
         <p style='color:#fcd34d;font-size:20px;'>💛 Jarvis — Tu asistente personal</p>
     </body>
     </html>
     """
 if __name__ == "__main__":
     app.run(host='0.0.0.0', port=10000)
