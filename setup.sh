AUTH0_DOMAIN = 'fsndprojects.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'capstone'
CLIENT_ID='UJIrZY4dlFXnqiyPfifWLI9Oy1BA8Q31'
database_name = "capstoneproject"
database_path = "postgresql://{}@{}/{}".format('postgres:1996', 'localhost:5432', self.database_name)
casting_assistant_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlYjFiNWIwNzYwMDZhZjRjMDFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0NDc3MDksImV4cCI6MTYzMDQ1NDkwOSwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.lMyHWn00-5nns0q9IGDwOSwteDcFRftz0DYT-XZ8XI7sSJywneQchc40smHX6-rYR1bDVdnyLX0ZodJX1MXkRrJ2-UVFZV9O4iBaTYHkcqxTUCm1u-ZV_7-8kp3vriM-2lmGvZ5L9XjLJ-bywP8zYMc19rOvKPOC8b-06n2Rrxqg0oGT06hjA5YWbPE8ZwXTlNdU2XqR9ifXoKGFDYvhl0PYuhm85BEok2FOoIsAC3W2MkxSuDNdmkV_9dSJ0aJI-_N5fwprujf5mR3mXAr8QjrywKGGj2Xd56M-DRkITXx7uHvlrQm__FbMZ2PErlL5awc0ll_vocge2bwbEPmCsg'
casting_director_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlNmQ4ZmM0YmEwMDcxZjBmNGY3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0NDczNjMsImV4cCI6MTYzMDQ1NDU2MywiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.h6-Ao69ZpHkT_O3AkDS_zZMkVpQcxvgmh2-XcumrNwPYQ0k9Zpi4X6kpEjOqDYZ3I2FTF9tO0dkqvB_bEhqmX0uzSXvEF11R5OKiClO7smRmTN3Q7U_J8_KeSHayVIIMXhDqAiLJl0FkRQ7e9thdnfkdbeZhEkreiyT7-SIAVFkAZnWoGzC24dEQ5uhMd1XY3hjxcD07ImjUnyms6zA4Jpa8ycZZzEoJfsHtg86CyWxMLl8ezoAwbmP_V5v7koWWyrY0f9MwvXTA6GItv4CjHplET1fAS7e6zdxwfP_xUqreOrB1pb3lLsDeugE7kvduaGbYmmLzlNIoH2QKL7OPjg'
executive_producer_jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Iko2bFB3Q3Y5YlN4SWd6MXZqN1pENSJ9.eyJpc3MiOiJodHRwczovL2ZzbmRwcm9qZWN0cy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEyYzFlYjFiNWIwNzYwMDZhZjRjMDFlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzA0NDc1MjksImV4cCI6MTYzMDQ1NDcyOSwiYXpwIjoiVUpJclpZNGRsRlhucWl5UGZpZldMSTlPeTFCQThRMzEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.kegyRdCAJExiild6zXke6S1wZX2CTuN0G0grr25FUJi3htuR5QrNKui0umg_miF3Tqn8KpjZknEphYybq7VdPibRJykuwc_nubpVNAeFCmPrd_01b8SioXL90ERmRFENoZs7WJPmHH1JOIwnRExlFbDx6MePu7_iWm4HpMttCQBYrRh1Ch-xLTndl8TS1wTiSNi8tnn1IJmblsmmNrs8H3K2p4HDox84Ppr1v0gQWe9TksXEjLcRu7QBII8ee5-cl4YEmKhJVUAQkiSG0n3khOhn_7DT-g6yvHcaa7Wexran00PFNd7DdyqznQ2dJ6W_jKwztrIAWxqr2TJTs-co2g'