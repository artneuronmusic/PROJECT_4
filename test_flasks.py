import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db
from settings import DB_NAME, CASTING_ASSIS, CASTING_DIRECTOR, PRODUCER



class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = DB_NAME
        self.database_path = "postgresql:///{}".format(self.database_name)
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
    
    '''
    test invalid token for get, post, patch, delete
    '''
    def test_get_castings_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().get("/castings", headers=headers_auth)
        
        self.assertEqual(res.status_code, 401)

    def test_get_movies_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().get("/movies", headers=headers_auth)
        
        self.assertEqual(res.status_code, 401)

    def test_post_movies_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().post("/movies/create", headers=headers_auth, 
        json={"title": "The Devil Wears Prada", "release_date": "2006-06-22"})
        
        self.assertEqual(res.status_code, 401)

    def test_post_castings_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().post("/castings/create", headers=headers_auth,  
        json={"name": "Meryl Strep", "age": 72, "gender": "Female"})
        
        self.assertEqual(res.status_code, 401)

    def test_patch_movies_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().patch("/movies/3/edit", headers=headers_auth, 
        json={"title": "The Devil Wears Versace", "release_date": "2006-06-22"})
        
        self.assertEqual(res.status_code, 401)

    def test_patch_castings_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().patch("/castings/3/edit", headers=headers_auth,  
        json={"name": "Meryl Strep", "age": 72, "gender": "Female"})
        
        self.assertEqual(res.status_code, 401)

    def test_delete_movies_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().delete("/movies/5", headers=headers_auth)
        
        self.assertEqual(res.status_code, 401)

    def test_delete_castings_list_notvalid_token(self):
        token = "Bearer " + "hfedkjkjnksnkn"
        headers_auth = {"Authorization": token}
        res = self.client().delete("/castings/5", headers=headers_auth)
        
        self.assertEqual(res.status_code, 401)


    '''
    assistant GET movies and castings list
    '''
    def test_assistant_get_castings_list_valid_token(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().get("/castings", headers=headers_auth)
        
        self.assertEqual(res.status_code, 200)

    def test_assistant_get_movie_list_valid_token(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().get("/movies", headers=headers_auth)
        
        self.assertEqual(res.status_code, 200)

    '''
    assistant POST movies and castings list
    '''
    def test_assistant_post_castings_no_permission(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().post("/castings/create", headers=headers_auth, 
        json={"name": "Meryl Streep", "age": 72, "gender": "Female"})
        
        self.assertEqual(res.status_code, 403)

    def test_assistant_post_movies_no_permission(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().post("/movies/create", headers=headers_auth, 
        json={"title": "The Devil Wears Prada", "release_date": "2006-06-22"})
        
        self.assertEqual(res.status_code, 403)

    '''
    assistant DELETE movies and castings list
    '''
    def test_assistant_delete_castings_no_permission(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().delete("/castings/1", headers=headers_auth)
   
        self.assertEqual(res.status_code, 403)

    def test_assistant_delete_movies_no_permission(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().delete("/movies/13", headers=headers_auth) 
    
        self.assertEqual(res.status_code, 403)


    ''' 
    assistant PATCH movies and castings list
    '''
    def test_assistant_patch_castings_no_permission(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().patch("/castings/2/edit", headers=headers_auth, 
        json={"name": "Gal Gadot-Varsano", "age": 37, "gender": "Female"})
        
        self.assertEqual(res.status_code, 403)

    def test_assistant_patch_movies_no_permission(self):
        token = "Bearer " + CASTING_ASSIS
        headers_auth = {"Authorization": token}
        res = self.client().patch("/movies/11/edit", headers=headers_auth, 
        json={"title": "Shang-Chi", "release_date": "2021-09-03"})
        
        self.assertEqual(res.status_code, 403)

  
    '''
    director GET movies and castings list
    '''
    def test_director_get_castings_list_valid_token(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().get("/castings", headers=headers_auth)
        
        self.assertEqual(res.status_code, 200)

    def test_director_get_movie_list_valid_token(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().get("/movies", headers=headers_auth)
        
        self.assertEqual(res.status_code, 200)

    '''
    director POST movies and castings list, 
    casting:{"name": "Natalie Portman", "age": 41, "gender": "Female"}
    movie: "title": "The Devil Wears Prada", "release_date": "2006-06-22"}
        
    '''
    def test_director_success_post_castings_permission(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().post("/castings/create", headers=headers_auth, 
        json={"name": "Natalie Portman", "age": 41, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_director_failure_post_castings_no_name(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().post("/castings/create", headers=headers_auth, 
        json={"name": "", "age": 72, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_director_post_movies_no_permission(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().post("/movies/create", headers=headers_auth, 
        json={"title": "The Devil Wears Prada", "release_date": "2006-06-22"})
        
        self.assertEqual(res.status_code, 403)


    '''
    director PATCH movies and castings list, use Gal Gadot, id 2, Shang-Chi, id11
    '''
    def test_director_success_patch_castings_permission(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().patch("/castings/2/edit", headers=headers_auth, 
        json={"name": "Gal Gadot-Varsano", "age": 72, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_director_failure_patch_castings_no_name(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().patch("/castings/2/edit", headers=headers_auth, 
        json={"name": "", "age": 37, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_director_patch_movies_no_permission(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().patch("/movies/11/edit", headers=headers_auth, 
        json={"title": "Shang-Chi", "release_date": "2021-09-03"})
        
        self.assertEqual(res.status_code, 200)

    '''
    director DELETE movies and castings list, casting id 1,  movie 13
    '''
    def test_director_success_delete_castings_permission(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().delete("/castings/1", headers=headers_auth) 
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_director_failure_delete_castings_no_id(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().delete("/castings/1000", headers=headers_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request')
        self.assertEqual(data['success'], False)

    def test_director_failure_delete_movies_no_permission(self):
        token = "Bearer " + CASTING_DIRECTOR
        headers_auth = {"Authorization": token}
        res = self.client().delete("/movies/1", headers=headers_auth) 
        
        self.assertEqual(res.status_code, 403)

    '''
    producer GET movies and castings list
    '''
    def test_producer_get_castings_list_valid_token(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().get("/castings", headers=headers_auth)
        
        self.assertEqual(res.status_code, 200)

    def test_producer_get_movie_list_valid_token(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().get("/movies", headers=headers_auth)
        
        self.assertEqual(res.status_code, 200)


#     '''
#     producer PATCH movies and castings list, topgun, id 17, Monica Anna Maria Bellucci, id6
#     '''
    def test_producer_success_patch_movies_permission(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().patch("/movies/17/edit", headers=headers_auth, 
        json={"title": "Top Gun", "release_date": "1986-05-16"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_success_patch_castings_permission(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().patch("/castings/6/edit", headers=headers_auth, 
        json={"name": "Monica Anna Maria Bellucci", "age": 58, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 403)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_failure_patch_movies_no_title(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().patch("/movies/17/edit", headers=headers_auth, 
        json={"title": "", "release_date": "1986-05-16"})
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], "bad request")

    def test_producer_failure_patch_castings_no_name(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().patch("/castings/6/edit", headers=headers_auth, 
        json={"name": "", "age": 59, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], "bad request")

    

#     '''
#     producer POST movies and castings list
#     '''
    def test_producer_success_post_movies_permission(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().post("/movies/create", headers=headers_auth, 
        json={"title": "Black Swan", "release_date": "2010-09-01"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_success_post_castings_permission(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().post("/castings/create", headers=headers_auth, 
        json={"name": "Juliette Binoche", "age": 58, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 403)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_failure_post_movies_no_title(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().post("/movies/create", headers=headers_auth, 
        json={"title": "", "release_date": "1988-10-14"})
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], "bad request")

    def test_producer_failure_post_castings_no_name(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().post("/castings/create", headers=headers_auth, 
        json={"name": "", "age": 59, "gender": "Female"})
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], "bad request")


    '''
    producer DELETE movies and castings list, movie,id2, casting id 4
    '''
    def test_producer_success_delete_movies_permission(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().delete("/movies/2", headers=headers_auth)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_success_delete_castings_permission(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().delete("/castings/4", headers=headers_auth)
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 403)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_producer_failure_delete_movies_no_id(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().delete("/movies/10000", headers=headers_auth)
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], "bad request")

    def test_producer_failure_delete_castings_no_id(self):
        token = "Bearer " + PRODUCER
        headers_auth = {"Authorization": token}
        res = self.client().delete("/castings/10000", headers=headers_auth)
        data = json.loads(res.data)
        
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], "bad request")




if __name__ == "__main__":
    unittest.main()
