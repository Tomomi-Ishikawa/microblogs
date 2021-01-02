from django.test import TestCase, Client

class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_accses(self):
        #self.assert_(True)
        
        # status code => 200 OK
        # status code => 302 Redirect
        # status code => 404 Not Found
        res = self.c.get('/')
        self.assertEqual(200, res.status_code)

    def test_fail_accsess(self):
        res = self.c.get('/unknow')
        self.assertEqual(404, res.status_code)