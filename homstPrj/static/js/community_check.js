document.getElementById('submitComment').addEventListener('click', function() {
    const commentText = document.getElementById('commentText').value;

    if (commentText.trim() !== '') {
        // 새 댓글을 화면에 추가
        const commentsSection = document.getElementById('comments-section');
        const newComment = document.createElement('article');
        newComment.innerHTML = `
            <div class="parent">
                <div class="parent-profile">
                    <img src="./img/mypage_profile.svg" class="profile-img">
                    <h3 class="name">yeeun</h3>
                </div>
                <p>${commentText}</p>
                <button>답글달기</button>
            </div>
        `;

        // 새 댓글을 목록의 맨 위에 추가 (내림차순 정렬)
        commentsSection.insertBefore(newComment, commentsSection.firstChild);

        // 입력 필드 초기화
        document.getElementById('commentText').value = '';
    }
});
