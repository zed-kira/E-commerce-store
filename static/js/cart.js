let update_btns = document.getElementsByClassName('add-to-cart');
let item_length = document.getElementsByClassName('change-quantity');

function add_listner(element) {
    for(let i = 0; i < element.length; i++){
        element[i].addEventListener('click', function(){
            let productID = this.dataset.product; // to get data-product value from html
            let action = this.dataset.action; // to get data-action value from html

            if (user == 'AnonymousUser') {
                console.log("not logged in !!");
            } else {
                updateUserCart(productID, action);
            }
        })
    }
}
add_listner(update_btns);
add_listner(item_length);

function getLoginUrl() {
    let url = '/accounts/login/';
}

function updateUserCart(productID, action){
    let url = '/update_cart/'

    fetch(url, { 
        method: 'POST', 
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID':productID, 'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        let cart_len = document.getElementById('cart_len');
        let res_data = data.split(" ");
        cart_len.innerHTML = res_data[0];
        let cart_item = document.getElementById('demo-delete');
        //if (action == "delete") { cart_item.remove(); };
        if (action == "delete") {
            cart_item.remove();
        } else {
            let item_length = document.getElementById(productID);
            let item_price = document.getElementsByClassName('cart_total_price');
            if (res_data[1] == 0) {
                cart_item.remove();
            } else {
                item_length.value = res_data[1];
                for (let i = 0; i < item_price.length; i++){
                    if (item_price[i].id == productID) {
                        item_price[i].innerHTML = res_data[2];
                    }
                }
            }
        }
    });
}

