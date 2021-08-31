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
        database_path = os.environ['DATABASE_URL']
        if database_path.startswith("postgres://"):
         database_path = database_path.replace("postgres://", "postgresql://", 1)
        setup_db(self.app, self.database_path)
        
        self.casting_assistant_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFkOGJiNWIwNzYwMDZhZjRiZmZmIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0MzUwMjksImV4cCI6MTYzMDQ0MjIyOSwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.hue_5DR66uGI69UrmZo70d_1cVMA0O5PmgkuyIUQ63npqc1PpX94VhPED2ZQaz04BaIuRQJ2Z9h3j57mZ6ttySyQdNXHXSGvXPFfx5C-UbzzNU-Rm7I7RTWX7QzmAR_mKUlgbkvQTjIeEiUmxVpZI0Y9EusFewYvSLqhT8XZuob9U_fHxILw2llXHPeUJx1CP-webM1VBK2s3sPUgP9AUqh3muBdodIaRL0ot2oxUYvMuhDoThwli2PaXtkd9WPIaOiN0Y0wsjnOT4KC8TsMTbbtbuNAee381s9lZZerntraBEpwE7Cno02fRCSx4OnVr5uf5FL7ULuEdTUU8v6y0g'
        }

        self.casting_director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlNmQ4ZmM0YmEwMDcxZjBmNGY3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0MzQ4NTIsImV4cCI6MTYzMDQ0MjA1MiwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.hV7KtVxvjchKMX7msi9Rz9qvNJlmyA9QYh6m8LUxVORvdxI6EqCZu7bLbsLS0QZoQ_yNc1PXymXsnWwnlbZ4yU3U1E56VhopYUumQ3E8esD2hHHQJp7FqAFok_3T3xv5HJL7HMBIQ9UCn-5Hz1ScKGHSd8h4pzBUiaagu7d7gtIOBpctzXZoKawo7En-wF2oLgt086u9XD1920qKurIsEgAkSj2lvKdjvX688enT7Nw4fZdr4iuv48jspZikvsT-CJaX_EnmKlbJL71pJu6wIJhYuB1mYaojSMfVjpSWDY9JwuQRRw8FgqTCM4A-Msw-sBEGhcOiK5MFHs6gHn0mNw'
        }

        self.executive_producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlYjFiNWIwNzYwMDZhZjRjMDFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0MzQ1NzUsImV4cCI6MTYzMDQ0MTc3NSwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.k7lnt1jOquTr_GlPonqif9epZ_V46_FS943NaYRGkkJr46p6empyvsFVuEJazmhckAdpfgAQBUdEsi7uW_VQWWGOrfYQb49iEn0TCgMU11QO-CplT6TZz8lJjQDOdAA-DCpC1LxvKGoUFoVi2f_X2bymad5muW-D_hHpkR9yaGnwo1CszY1wUpk49PW1t0x2PdX67CE4ONnALsKnGpf3qcrWuia7PaSJg9JnYqM9ue2uxnUTLGQAhYV6WOtotr7NfURFtj8u-8XJh2gWI9RJNwxbIPWquUUr6XAQ8fmj2vrMpynJ98VKf286Nnigml9JITg4w7Of_QeX0BqK9njhhA'
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