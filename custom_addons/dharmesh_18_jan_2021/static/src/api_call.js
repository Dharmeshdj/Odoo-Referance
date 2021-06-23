

console.log("this function is call");

function api_call(){
    var $data=$('#datas');
    $.ajax({
        type: "GET",
        url: "https://jsonplaceholder.typicode.com/todos/1",
        success: function(data) {
            
            console.log('success',data);
            $data.append('<tr><td>'+data.id+'</td>'+'<td>'+data.title+'</td>'+'<td>'+data.completed+'</td></tr>')
            $data.hide(2000).delay(1000).show(2000);
            $data.css({color:'red'})
            },
        error: function(){
            alert("error acured")
            }
        });
    
        };
