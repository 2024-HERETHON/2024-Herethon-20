# 2024-Herethon-20
2024 여기톤 : HERETHON 20조


- **서비스 소개**

  HOMST 홈스트 

  홈스트는 여성들을 위해 안심 숙소 추천 및 예약을 돕고, 
  안전한 여행/숙박 문화를 공유하는 플랫폼입니다. 
  
  안심필터를 통해 숙박시설을 검색하고 예약할 수 있습니다. 
  또한 숙소에 대한 더 구체적인 후기나 여행에 대한 후기도 남기며 다른 유저들과 소통할 수도 있습니다. 
  
  여성들이 숙박, 여행 중 겪을 수 있는 불안감을 해소하고 
  건강한 숙박 문화를 함께 조성해나갈 수 있는 HOMST 홈스트입니다.

- **기술 스택**

  <span>프론트엔드: </span> <img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

  <span>백엔드: </span><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=Django&logoColor=white">

  <span>기획·디자인: </span> <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">

- **팀원 소개**
  <table border="" cellspacing="0" cellpadding="0" width="100%">
  <tr width="100%">
  <td align="center">최예은</a></td>
  <td align="center">강나연</a></td>
  <td  align="center">강신영</a></td>
  <td  align="center">권가영</a></td>
  <td  align="center">엄서희</a></td>
  <td  align="center">최유연</a></td>
  </tr>
  <tr width="100%">
  <td  align="center"><a href="https://imgbb.com/"><img src="https://github.com/2024-HERETHON/2024-Herethon-20/assets/143514087/96ba0388-eda0-4ef6-ac97-1f86c2bc7a56" alt="befbedf87e51f5b02aac8b882ada60fd-sticker" border="0" width="90px"></a></td>
  <td  align="center"><a href="https://imgbb.com/"><img src="https://github.com/2024-HERETHON/2024-Herethon-20/assets/143514087/8f69346a-8659-4287-ac4e-76d0c0294918" alt="befbedf87e51f5b02aac8b882ada60fd-sticker" border="0" width="90px"></a></td>
  <td  align="center"><a href="https://imgbb.com/"><img src="https://github.com/2024-HERETHON/2024-Herethon-20/assets/143514087/1055a493-3e72-453f-81d0-b5c4922efcf6" alt="f67635fddb50d05f2d0f142e63b0ab5c-sticker" border="0" width="90px"></a></td>
  <td  align="center"><a href="https://imgbb.com/"><img src="https://github.com/2024-HERETHON/2024-Herethon-20/assets/143514087/e72a22f3-12fa-4d02-834b-95337abb6a74" border="0" width="100px"></a></td>
  <td  align="center"><a href="https://imgbb.com/"><img src="https://github.com/2024-HERETHON/2024-Herethon-20/assets/143514087/5f1fe5d8-e3c2-453c-bb94-72beeac0ae45" border="0" width="70px"></a></td>
  <td  align="center"><a href="https://imgbb.com/"><img src="https://github.com/2024-HERETHON/2024-Herethon-20/assets/143514087/3ab18332-30d5-409e-8418-1ac392a269fa" border="0" width="90px"></a></td>
    
  </tr>
  <tr width="100%">
  <td  align="center">기획·디자인</td>
  <td  align="center">프론트엔드</td>
  <td  align="center">프론트엔드</td>
  <td  align="center">백엔드</td>
  <td  align="center">백엔드</td>
  <td  align="center">백엔드</td>
     </tr>
      <tr width="100%">
          <td  align="center"><p>서비스 기획</p><p>UI 디자인</p><p>서비스 발표</p></td>
          <td  align="center"><p></p>커뮤니티 구현<p>마이페이지 구현</p></td>
          <td  align="center"><p>회원가입/로그인</p><p>숙소 검색 및 결과</p></td>
          <td  align="center"><p>메인페이지 구현</p><p>검색기능 필터</p><p>커뮤니티 댓글/좋아요</p></td>
          <td  align="center"><p>커뮤니티 CRUD</p><p>admin 저장</p><p>url연결</p></td>
          <td  align="center"><p>회원가입/로그인</p><p>admin 저장</p><p>마이페이지</p></td>
     </tr>
  </table>

- **폴더 구조**

  ```
  📂 homst
  └─ 2024-Herethon-20
   ├─ homePrj
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   ├─ accounts
   │  ├─ templates
         └──login.html
         └──signup.html
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py 
   │  └─ views.py
   ├─ homst
   │  ├─ templates
         └──community.html
         └──community_create.html
         └──community_delete.html
         └──community_detail.html
         └──community_update.html
         └──main.html
         └──mypage.html
         └──record_detail.html
         └──reserve.html
         └──reserveok.html
         └──search_results.html
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ forms.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py 
   │  └─ views.py
   └─ manage.py
  ```

- **개발환경에서의 실행 방법**
  ```
  $ django-admin startproject homstPrj
  $ python manage.py runserver
  ```
  <hr/>
