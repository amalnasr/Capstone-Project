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
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFkOGJiNWIwNzYwMDZhZjRiZmZmIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0NTYzMjUsImV4cCI6MTYzMDQ2MzUyNSwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.krF3hakOUL0ttJOKsoAStOkhEFQbxRCQBz3P1Bqi0xOKPooZ79gZ5XYFj_dWQd3lvCcf_S1rGJkzJIbQKMZaO_aywx0l-oI1Q0P4j88b-ZEvxyHbk3Mwm92-Zd9DVFVxUxby8DdesCHIFrBKfwMwT6RB-r4CeGpnNL5k2Qlw8Cm7JfFJU3G2-pO2dsRk__op3X12jUCcZnkFyvJuemYUvrHPHAEmn2PpSmcBvsiU4KNnnTLqSLPsq6tlTjeUk0B7_GH13eLjfBHrqVzI21zIYLNU0SGU_HJsHVt6FZEDEUnEwzdfqlRt68c7apDkmxg1Npij_Vns4NLgdV1rrFyykg'
        }

        self.casting_director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlNmQ4ZmM0YmEwMDcxZjBmNGY3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0NTYyMjMsImV4cCI6MTYzMDQ2MzQyMywiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.fyxaQckxRevEuNPDJwaDBO9HyGD3Po5_Kp78gp3PmhJoJQpGZ7xykQt0RjWXhXqajrDQ-ZiWw90AtTZCMiExjrM9sAAYbkXJzLjETnm_bcox-K86F_e39oRTtCFoK2BYRDSHrSYTSyCj-7-9rljzbTRSqHTuSGRd-ZMHUsWLU5I-tftqCFuARqm8lefTyrhC4kxe14NYQZduTsTmufTgWTX3nrsRalAOkOP0OXnXh3cHBWDJCireiOJ9zqGuUTY88yEoB70BXXyTvaINaekaU0ThZa7gcQzUO7OqXgIkRQOj0XSTR9QH8T6NQDkjX0KByuEL3z-MM7q2n15y8ci3cQ'
        }

        self.executive_producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlYjFiNWIwNzYwMDZhZjRjMDFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0NTU1NjIsImV4cCI6MTYzMDQ2Mjc2MiwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.BIP0kyLL6LOy5F5dZdcSzwztnjhLbrwBRzpxDwPmRG33Ysz33tJghWY5QSlEmuPkC_ZVHdGJlvGVJxFAoeE3J0B6VQy64ayuc4iN-iaESsuouVzNq8iTYLX6-pWIIdYilluRv0UjA0p-Q07ng-qPE5qA5dPSafgevVc49nsFZMx8Ex8X1KJ_lJ9Nb2Uv4mAPhoLsQDHXezH5Qq8DXq7Ob--thEeQfLm-9B2AxiD4fmThN6tw1rBjVGBH05WbCstPyYlD5AzcHRUjjRJI_spWKR0yeguQsNLOp9qX1T8TzH6p-bIRSGFMR6m-3TOAZuKpMW9J8iETzg923keFCv7RdA'
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