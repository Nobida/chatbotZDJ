
## 知道君知识图谱项目(测试用)
python3 manage.py runserver:0.0.0.0:8001 启动

功能名|说明
---|---
智能问答|该功能实现原理为多搜索引擎爬虫+neo4j数据库节点遍历。当用户发送固定结构的问句，如”印度的首都是“时，程序首先通过百度知识图谱进行查询及百度百科inforbox中进行查询，若查询不到，则调用服务器neo4j数据库进行节点匹配查询
相关节点返回|
最短路径返回|
节点网络返回|


----------

## 接口服务示例：
### 智能问答
```
import requests

def main():
    res = requests.post('http://127.0.0.1:8001/query/', data={'query':'印度的首都是'})
    print(res.text)

if __name__ == "__main__":
    main()

response: {"res": "新德里"}
```

### 相关节点返回

```
import requests

def main():
    res = requests.post('http://127.0.0.1:8001/related/', data={'entity':'孔'})
    print(res.text)

if __name__ == "__main__":
    main()

response: {"res": [["孔子", "177"], ["孔鲤", "2146"], ["孔门十二哲", "2755"], ["孔子家语", "2795"]]}
```
### 最短路径返回

```
import requests

def main():
    res = requests.post('http://127.0.0.1:8001/shortestpath/', data={'entity1':'孔子','entity2':'论语'})
    print(res.text)

if __name__ == "__main__":
    main()

response : {"res": ["<Record r=[(子思)-[:孙子 {}]->(孔子), (孟子)-[:继承 {}]->(子思), (四书)-[:包含 {}]->(孟子), (四书)-[:包含 {}]->(论语)] p1.uuid='177' p2.uuid='232'>"]}

```
### 节点网络返回

```
import requests

def main():
    res = requests.post('http://127.0.0.1:8001/network/', data={'entity':'孔子','lim_num':3})
    print(res.text)

if __name__ == "__main__":
    main()

response: {"res": ["<Record r=(曾子)-[:继承 {}]->(孔子) p1.uuid='177' p2.uuid='109'>", "<Record r=(孔子)-[:整理 {}]->(诗经) p1.uuid='177' p2.uuid='2208'>", "<Record r=(子思)-[:孙子 {}]->(孔子) p1.uuid='177' p2.uuid='110'>"]}
```
----------


