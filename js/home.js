const hotels = [
    { name: '숙소 호텔 청초', price: '76,000원', rating: '4.0', tag: '여성 전용 숙소', pic: '../asset/img/home_list_img1.svg'},
    { name: '제주 블루오션 호텔', price: '106,000원', rating: '4.3', tag: ' ', pic: '../asset/img/home_list_img2.svg'},
    { name: '제주 우드포레스트 숙박', price: '74,000원', rating: '3.5', tag: ' ', pic: '../asset/img/home_list_img3.svg'},
    { name: '가평 모닥불 펜션', price: '64,000원', rating: '4.0', tag: '여성 전용 숙소', pic: '../asset/img/home_list_img4.svg'}
];
const hotel = [
    { name: '제주 화이트 펜션', price: '79,000원', rating: '4.7', tag: ' ', pic: '../asset/img/home_list_img5.svg'},
    { name: '속초 골든튤립', price: '54,000원', rating: '4.5', tag: '여성 전용 숙소', pic: '../asset/img/home_list_img6.svg'},
    { name: '속초 브릿지 호텔', price: '82,000원', rating: '4.0', tag: ' ', pic: '../asset/img/home_list_img7.svg'},
    { name: '속초 모던시티 호텔', price: '73,000원', rating: '4.0', tag: '여성 전용 숙소', pic: '../asset/img/home_list_img8.svg'}
];

const hotelList = document.getElementById('home_lists');
const hotelbestList = document.getElementById('home_best_lists');

hotels.forEach(hotel => {
    const hotelItem = document.createElement('div');
    hotelItem.className = 'home_list';

    hotelItem.innerHTML = `
        <div class="home_list_img" style="background-image: url('${hotel.pic}');"> <div class="home_list_heart" style="background-image: url('../asset/svg/home_list_heart.svg');"></div> </div>
            <div class="home_list_name_div">
                <div class="home_list_name_txt">
                    <div class="home_list_name_type">${hotel.tag}</div>
                    <div class="home_list_name">${hotel.name}</div>
                </div>
                <div class="home_list_name_rec">
                    <img src="../asset/svg/home_list_name_rec_icon.svg" class="home_list_name_rec_icon" alt="">
                    <p class="home_list_name_rec_num">${hotel.rating}</p>
                </div>
            </div>
        <h6 class="home_list_price">${hotel.price}</h6>
    `;

    hotelList.appendChild(hotelItem);
});

hotel.forEach(hotel => {
    const hotelbestItem = document.createElement('div');
    hotelbestItem.className = 'home_list';

    hotelbestItem.innerHTML = `
        <div class="home_list_img" style="background-image: url('${hotel.pic}');"> <div class="home_list_heart" style="background-image: url('../asset/svg/home_list_heart.svg');"></div> </div>
            <div class="home_list_name_div">
                <div class="home_list_name_txt">
                    <div class="home_list_name_type">${hotel.tag}</div>
                    <div class="home_list_name">${hotel.name}</div>
                </div>
                <div class="home_list_name_rec">
                    <img src="../asset/svg/home_list_name_rec_icon.svg" class="home_list_name_rec_icon" alt="">
                    <p class="home_list_name_rec_num">${hotel.rating}</p>
                </div>
            </div>
        <h6 class="home_list_price">${hotel.price}</h6>
    `;

    hotelbestList.appendChild(hotelbestItem);
});

document.addEventListener("DOMContentLoaded", () => {
    const filterButton = document.getElementById('home_head_filter');
    const filterDropdown = document.getElementById('home_head_filter_drop_div');

    filterButton.addEventListener('click', () => {
        filterDropdown.style.display = filterDropdown.style.display === 'block' ? 'none' : 'block';
    });

    document.addEventListener('click', (event) => {
        if (!filterButton.contains(event.target) && !filterDropdown.contains(event.target)) {
            filterDropdown.style.display = 'none';
        }
    });
});

