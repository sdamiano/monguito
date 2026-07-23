from datetime import datetime
from bson.objectid import ObjectId
from flask import Blueprint, redirect, render_template, request, url_for
from app.database import posts_collection

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def index():
    """READ: Lista todos los artículos del blog ordenados por fecha de creación desc."""
    posts = list(posts_collection.find().sort("fecha_creacion", -1))
    return render_template("index.html", posts=posts)


@blog_bp.route("/add", methods=["POST"])
def add_post():
    """CREATE: Agrega un nuevo artículo con contenido inicial y lista de comentarios embebida vacía."""
    titulo = request.form.get("titulo")
    autor = request.form.get("autor")
    contenido = request.form.get("contenido")

    if titulo and autor and contenido:
        posts_collection.insert_one({
            "titulo": titulo,
            "autor": autor,
            "contenido": contenido,
            "fecha_creacion": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "comentarios": []  # Documentos embebidos (Array de comentarios)
        })

    return redirect(url_for("blog.index"))


@blog_bp.route("/comment/<post_id>", methods=["POST"])
def add_comment(post_id):
    """EMBEDDED PUSH: Agrega un nuevo comentario dentro de la lista 'comentarios' del post en MongoDB."""
    try:
        obj_id = ObjectId(post_id)
        autor = request.form.get("autor_comentario")
        texto = request.form.get("texto_comentario")

        if autor and texto:
            # Usamos el operador $push de MongoDB para insertar en la lista embebida
            posts_collection.update_one(
                {"_id": obj_id},
                {"$push": {
                    "comentarios": {
                        "autor": autor,
                        "texto": texto,
                        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
                    }
                }}
            )
    except Exception:
        pass

    return redirect(url_for("blog.index"))


@blog_bp.route("/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """UPDATE: Obtiene el formulario de edición o actualiza el artículo por ObjectId."""
    try:
        obj_id = ObjectId(post_id)
    except Exception:
        return redirect(url_for("blog.index"))

    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        contenido = request.form.get("contenido")

        if titulo and autor and contenido:
            posts_collection.update_one(
                {"_id": obj_id},
                {"$set": {
                    "titulo": titulo,
                    "autor": autor,
                    "contenido": contenido
                }}
            )
        return redirect(url_for("blog.index"))

    post = posts_collection.find_one({"_id": obj_id})
    if not post:
        return redirect(url_for("blog.index"))

    return render_template("edit.html", post=post)


@blog_bp.route("/delete/<post_id>", methods=["POST"])
def delete_post(post_id):
    """DELETE: Elimina un artículo de MongoDB utilizando su ObjectId."""
    try:
        obj_id = ObjectId(post_id)
        posts_collection.delete_one({"_id": obj_id})
    except Exception:
        pass

    return redirect(url_for("blog.index"))
