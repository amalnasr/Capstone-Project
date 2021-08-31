import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "capstoneproject"
        # self.database_path = "postgresql://{}@{}/{}".format('postgres:1996', 'localhost:5432', self.database_name)
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)
        
        self.casting_assistant_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFkOGJiNWIwNzYwMDZhZjRiZmZmIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzAzNzAzNDIsImV4cCI6MTYzMDM3NzU0MiwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.cU7-YQaaCA-aocjtqMGq5h09DZRpXzRZ9rX5vgnwz6_citsEiDCxzzQqWORcLCLZstbQ0FhMtRnnhjFen13tETotaAHCMwEbrH3kKk_0lrm-izh91QHG8XBGoo86znI2SrC8DKxqqasqODAwFnef8CgPUMUCx_683OOB2CsUDttYP2xqiF0QWi7mfBqare35bJWbLE8KmEREpqWJLCtGjWMO-BXHMFpAVTVjOyWkChXir8L9jFYM8MK8GwXaqYSUnbwepEfJ1JF3ejkJVysONFBt4SL9ZVSibqSuMvHrHszr_jPM8EqWHjFiaF1gLT2obqHeVHFVOVKF-MxWefFBhg'
        }

        self.casting_director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlNmQ4ZmM0YmEwMDcxZjBmNGY3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzAzNzA5MjcsImV4cCI6MTYzMDM3ODEyNywiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.bcBO4chSomUZY7NOwN1qSXHFzlufGPaAih27eY5F8Um-cfCC_TqM_350S8tESBUbGy-rHNJaeeIa97mQ3zgzEGCXJaKZzVGOmXE6Dkz_IhzT79pRg7FtaLvfSLTl9l7LzXYmgU4Hbt6QdeFBs2ghZkgt3STdHaQShg3WxPF2sGitZX9r2sUB47XkRko8R3aRb6y77lxx17f2J7uCo3ZltRPgs42OjCflYaKeCMloos5APU745-6jYHoket8lNnF3oAEi2pkKeDpux57In0pDvwNR_l7Z5T16aJ7QnYVVlQJjx2Jc5mgH6ZMI_xYH-RzAY_sjLsZa4AoOKxsg7ySbsw'
        }

        self.executive_producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlYjFiNWIwNzYwMDZhZjRjMDFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzAzNzE0NDcsImV4cCI6MTYzMDM3ODY0NywiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.bY9uYOaek3-v9bD-xXakgq7HnAF6piBUVMQ3dfJG4ufmvDsIJonmVVme3pxHdHmk_TEmd9j_NDbkS5Sm1PtL8b-YZow_W-ThP3NEuxIhQ8lnJOItApBS-U71uFNe9Tl3fDIryEEhyNi8rTyF1TvXW6BGeoeDSrVSYxW73LYwYtN2tXo7Axh_-7KTM7Zt_9rkDvA_sBJGmV2zrYJBK65TPA8UBVgwCU9oW74HLRnqRoW_VWEjlMfGvg8THwkDE358d_rUTwYUUKg-377URBCWXoxnAaoge5-CbqC15oZCbOHviPn33Sx_GRX0ZVXSGAGwcEA2MuHjWovsG9Lo1W7hZA'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
 
    
    
    def tearDown(self):
        """Executed after reach test"""
        pass

# Test Get actors API

    def test_get_actors(self): # Test for success behavior
        res = self.client().get('/actors',
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_404_get_actors(self): # Test for error behavior
        res = self.client().get('/actors/',
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test Get movies API

    def test_get_movies(self): # Test for success behavior
        res = self.client().get('/movies',
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_404_get_movies(self): # Test for error behavior
        res = self.client().get('/movies/',
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test post new actor API

    def test_post_actors(self): # Test for success behavior
        new_test_actor = {
            "name": "actor test name",
            "age": 0,
            "gender": "Female"
        }
        res = self.client().post('/actors', json = new_test_actor, 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])

    def test_422_post_actors(self): # Test for error behavior
        new_test_actor = {
            "name": "actor test name",
            "age": "five",
            "gender": "Female"
        }
        res = self.client().post('/actors', json = new_test_actor,
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Test post new movie API

    def test_post_movies(self): # Test for success behavior
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json = new_test_movie, 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])

    def test_422_post_movies(self): # Test for error behavior
        new_test_movie = {
           "title": "movie test name",
           "release_date": "date"
        }
        res = self.client().post('/movies', json = new_test_movie,
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Test delet actor API

    def test_delete_actors(self): # Test for success behavior

        res = self.client().delete('/actors/2',  
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'], 2)
        self.assertEqual(actor, None)

    def test_404_delete_actors(self): # Test for error behavior
       
        res = self.client().delete('/actors/200', 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')  

# Test delet movie API

    def test_delete_movies(self): # Test for success behavior

        res = self.client().delete('/movies/2',  
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'], 2)
        self.assertEqual(movie, None)

    def test_404_delete_movies(self): # Test for error behavior
       
        res = self.client().delete('/movies/200', 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')  

# Test patch actor API

    def test_patch_actors(self): # Test for success behavior

        res = self.client().patch('/actors/1', json={'age': "33"}, 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_actor'])
       

    def test_404_patch_actors(self): # Test for error behavior
       
        res = self.client().delete('/actors/200',  json={'name': "updated actor name"},
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test patch movie API

    def test_patch_movies(self): # Test for success behavior

        res = self.client().patch('/movies/1', json={'title': "updated test movie title"}, 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_movie'])
       

    def test_404_patch_movies(self): # Test for error behavior
       
        res = self.client().delete('/movies/200',  json={'title': "updated movie title"},
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found') 

# Test RBAC for casting assistant role

    def test_get_actors_casting_assistant_role(self): # Test for authorized access
        res = self.client().get('/actors',
                                headers=self.casting_assistant_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_401_get_actors_casting_assistant_role(self): # Test for unauthorized access
        res = self.client().get('/actors')
        
        self.assertEqual(res.status_code, 401)

# Test RBAC for casting director role

    def test_get_actors_casting_director_role(self): # Test for authorized access
        new_test_actor = {
            "name": "actor name test role ",
            "age": 20,
            "gender": "Female"
        }
        res = self.client().post('/actors', json = new_test_actor, 
                                headers=self.casting_director_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])

    def test_401_get_actors_casting_director_role(self): # Test for unauthorized access
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json = new_test_movie, 
                                headers=self.casting_director_header)
        
        self.assertEqual(res.status_code, 401)

# Test RBAC for executive producer role

    def test_get_actors_executive_producer_role(self): # Test for authorized access
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json = new_test_movie, 
                                headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])
        
    def test_401_get_actors_executive_producer_role(self): # Test for unauthorized access
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json = new_test_movie)
        self.assertEqual(res.status_code, 401)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()