from flask_restful import Resource, Api

class Music(Resource):
    def get(self):
        music = [
            {
                'author': 'Eminem',
                'title': 'Till I Collapse',
                'album': 'Sing for the Moment',
                'year': '2002',
                'time': '4:57',
                'file_type': 'mp3'
            },
            {
                'author': 'Eminem',
                'title': 'My name is',
                'album': 'The Slim Shady LP',
                'year': '1999',
                'time': '4:28',
                'file_type': 'mp3'
            },
            {
                'author': 'Eminem',
                'title': 'The Real Slim Shady',
                'album': 'The Marshall Mathers LP',
                'year': '2000',
                'time': '4:44',
                'file_type': 'mp3'
            },
            {
                'author': 'Eminem',
                'title': 'Sing for the Moment',
                'album': 'The Eminem Show',
                'year': '2002',
                'time': '5:39',
                'file_type': 'mp3'
            }
        ]

        return music