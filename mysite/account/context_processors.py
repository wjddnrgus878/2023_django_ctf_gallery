def add_session_to_context(request):
    return {'id': request.session.get('id')}