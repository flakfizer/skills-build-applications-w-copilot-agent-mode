from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://solid-waddle-5rv595p59vfp69v-8000.app.github.dev/api/'
    return Response({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activity': base_url + 'activity/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/'
    })