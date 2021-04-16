from locust import HttpUser, TaskSet, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    

    @task
    def get_all_ap1(self):
        params = {"tag": "AGEN"}
    
        url1 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-1"
       
        self.client.get(url1,params = params,headers={"Authorization":  "eyJraWQiOiJIZzJDZDdYRzFFc3FQaWltU1NjcjRqUXBZcHVUXC81MTNpc3V4VW9DOUNWUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTQ1MjVna203NnV2dHZndHFsdTkxbWx1cyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidGVhbTUtY3N5ZTcyNDUtc2VydmVyLWlkXC9sYW1iZGEtaW52b2tlIiwiYXV0aF90aW1lIjoxNjE4NTk4OTYxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9mRFFoVTBKaWEiLCJleHAiOjE2MTg2ODUzNjEsImlhdCI6MTYxODU5ODk2MSwidmVyc2lvbiI6MiwianRpIjoiZWEwNzYyNTAtMzRiNC00ZWNiLWJhMmQtM2ViMmVmMmM5NzA3IiwiY2xpZW50X2lkIjoiMTE0NTI1Z2ttNzZ1dnR2Z3RxbHU5MW1sdXMifQ.dpFAVRdPLkgfv72I_3IILrkX4ctNSPjYGLv4m8aduvSs3wl8aKXtSzsC0uJz1twV7f-f5jL_8CNSLt3YWutRPAkAB4nEBZFQUlpiGB_XBmdLPKLaWvRbhDQrcAATV43sw0V64Z3zH7fHfAn6Lsz0aROj1GZQlM548pCWUWdNnzrQpyWBlwI0xHgeOnyGYd6b2qs7SfHLRuDvi2Gkj9YDxMDxdnL05NayUEovty9M8YkiuAunll6JDJ9O8Cy4ylOpEMfodYL7C6bjADb7YKEVJLJSLYkKZ98dhoCZZ2wf0ad-4EzyPNJzgczWIN5MMT1ChElECEc4JlbATUZj-UV6gw"})
       
    @task
    def get_all_ap2(self):
        params = {"tag": "AGEN"}
    
        url1 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-2"
       
        self.client.get(url1,params = params,headers={"Authorization":  "eyJraWQiOiJIZzJDZDdYRzFFc3FQaWltU1NjcjRqUXBZcHVUXC81MTNpc3V4VW9DOUNWUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTQ1MjVna203NnV2dHZndHFsdTkxbWx1cyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidGVhbTUtY3N5ZTcyNDUtc2VydmVyLWlkXC9sYW1iZGEtaW52b2tlIiwiYXV0aF90aW1lIjoxNjE4NTk4OTYxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9mRFFoVTBKaWEiLCJleHAiOjE2MTg2ODUzNjEsImlhdCI6MTYxODU5ODk2MSwidmVyc2lvbiI6MiwianRpIjoiZWEwNzYyNTAtMzRiNC00ZWNiLWJhMmQtM2ViMmVmMmM5NzA3IiwiY2xpZW50X2lkIjoiMTE0NTI1Z2ttNzZ1dnR2Z3RxbHU5MW1sdXMifQ.dpFAVRdPLkgfv72I_3IILrkX4ctNSPjYGLv4m8aduvSs3wl8aKXtSzsC0uJz1twV7f-f5jL_8CNSLt3YWutRPAkAB4nEBZFQUlpiGB_XBmdLPKLaWvRbhDQrcAATV43sw0V64Z3zH7fHfAn6Lsz0aROj1GZQlM548pCWUWdNnzrQpyWBlwI0xHgeOnyGYd6b2qs7SfHLRuDvi2Gkj9YDxMDxdnL05NayUEovty9M8YkiuAunll6JDJ9O8Cy4ylOpEMfodYL7C6bjADb7YKEVJLJSLYkKZ98dhoCZZ2wf0ad-4EzyPNJzgczWIN5MMT1ChElECEc4JlbATUZj-UV6gw"})


    @task
    def get_all_ap3(self):
        params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
    
        url1 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-3"
       
        self.client.get(url1,params = params,headers={"Authorization":  "eyJraWQiOiJIZzJDZDdYRzFFc3FQaWltU1NjcjRqUXBZcHVUXC81MTNpc3V4VW9DOUNWUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTQ1MjVna203NnV2dHZndHFsdTkxbWx1cyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidGVhbTUtY3N5ZTcyNDUtc2VydmVyLWlkXC9sYW1iZGEtaW52b2tlIiwiYXV0aF90aW1lIjoxNjE4NTk4OTYxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9mRFFoVTBKaWEiLCJleHAiOjE2MTg2ODUzNjEsImlhdCI6MTYxODU5ODk2MSwidmVyc2lvbiI6MiwianRpIjoiZWEwNzYyNTAtMzRiNC00ZWNiLWJhMmQtM2ViMmVmMmM5NzA3IiwiY2xpZW50X2lkIjoiMTE0NTI1Z2ttNzZ1dnR2Z3RxbHU5MW1sdXMifQ.dpFAVRdPLkgfv72I_3IILrkX4ctNSPjYGLv4m8aduvSs3wl8aKXtSzsC0uJz1twV7f-f5jL_8CNSLt3YWutRPAkAB4nEBZFQUlpiGB_XBmdLPKLaWvRbhDQrcAATV43sw0V64Z3zH7fHfAn6Lsz0aROj1GZQlM548pCWUWdNnzrQpyWBlwI0xHgeOnyGYd6b2qs7SfHLRuDvi2Gkj9YDxMDxdnL05NayUEovty9M8YkiuAunll6JDJ9O8Cy4ylOpEMfodYL7C6bjADb7YKEVJLJSLYkKZ98dhoCZZ2wf0ad-4EzyPNJzgczWIN5MMT1ChElECEc4JlbATUZj-UV6gw"})
       