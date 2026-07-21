from ninja import Router

router = Router()

@router.get('/')
def home(request):
    return 1