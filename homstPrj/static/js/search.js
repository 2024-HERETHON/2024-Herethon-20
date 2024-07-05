const search_hotels = [
    { name: '숙소 호텔 청초', price: '94,000원', rating: '9.0', tag: '여성 전용 숙소'},
    { name: '숙소 호텔 청초', price: '94,000원', rating: '9.0', tag: '여성 전용 숙소'},
    { name: '숙소 호텔 청초', price: '94,000원', rating: '9.0', tag: '여성 전용 숙소'},
    { name: '숙소 호텔 청초', price: '94,000원', rating: '9.0', tag: '여성 전용 숙소'}
];

const search_hotelList = document.getElementById('search_result_lists');

search_hotels.forEach(hotel => {
    const hotelItem = document.createElement('div');
    hotelItem.className = 'search_result_list';

    hotelItem.innerHTML = `
        <div class="search_result_img"></div>
                    <div class="search_result_imp">
                        <div>
                            <p class="search_result_home_type">${hotel.tag}</p>
                            <p class="search_result_name">${hotel.name}</p>
                            <p class="search_result_where">속초시, 역 도보 8분</p>
                            <div class="search_result_rec">
                                <img src="../asset/svg/home_list_name_rec_icon.svg" class="search_result_rec_icon" alt="">
                                <p class="search_result_rec_num">${hotel.rating}</p>
                            </div>
                        </div>
                        <div class="search_result_under">
                            <div class="search_result_types">
                                <p class="search_result_type">CCTV 사각지대 최소</p>
                                <p class="search_result_type">여성전용 숙소</p>
                                <p class="search_result_type">개별 화장실</p>
                            </div>
                            <div class="search_result_price">
                                <p class="search_result_price_txt">전 객실 평균</p>
                                <p class="search_result_price_num">${hotel.price}</p>
                            </div>
                        </div>
                    </div>
    `;

    search_hotelList.appendChild(hotelItem);
});


const inputLeft = document.getElementById("input-left");
const inputRight = document.getElementById("input-right");

const thumbLeft = document.querySelector(".thumb.left");
const thumbRight = document.querySelector(".thumb.right");

const range = document.querySelector(".range");

const setLeftValue = e => {
  const _this = e.target;
  const { value, min, max } = _this;

  if (+inputRight.value - +value < 10) {
    _this.value = +inputRight.value - 10;
  }

  const percent = ((+_this.value - +min) / (+max - +min)) * 100;

  thumbLeft.style.left = `${percent}%`;
  range.style.left = `${percent}%`;
};

const setRightValue = e => {
  const _this = e.target;
  const { value, min, max } = _this;

  if (+value - +inputLeft.value < 10) {
    _this.value = +inputLeft.value + 10;
  }

  const percent = ((+_this.value - +min) / (+max - +min)) * 100;

  thumbRight.style.right = `${100 - percent}%`;
  range.style.right = `${100 - percent}%`;
};

if (inputLeft && inputRight) {
  inputLeft.addEventListener("input", setLeftValue);
  inputRight.addEventListener("input", setRightValue);
}