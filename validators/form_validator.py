from constants.file import ALLOWED_IMAGE_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def validate_form(request):
    errors = []

    # START - VALIDATE FILE
    file = request.files.get('file')
    if not file:
        errors.append("El archivo es obligatorio.")
    elif not allowed_file(file.filename):
        errors.append("El archivo debe ser de tipo jpeg, png o jpg.")
    # END - VALIDATE FILE

    # START - VALIDATE DESCRIPTION
    description = request.form.get('description')
    if not description:
        errors.append("La descripción es obligatorio.")
    elif len(description) < 5:
        errors.append("La descripción debe tener al menos 5 caracteres.")
    # END - VALIDATE DESCRIPTION

    # START - VALIDATE NAME
    name = request.form.get('name')
    if not name:
        errors.append("El nombre es obligatorio.")
    elif len(name) < 5:
        errors.append("El nombre debe tener al menos 5 caracteres.")
    # END - VALIDATE NAME

    # START - VALIDATE TAGS
    tags = request.form.getlist('tags')  # Flask soporta listas con `getlist`
    if not tags:
        errors.append("El campo 'tags' es obligatorio.")
    elif len(tags) < 1:
        errors.append("El campo 'tags' debe contener al menos un elemento.")
    # END - VALIDATE TAGS

    return errors
