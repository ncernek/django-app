var React = require('react')
var ReactDOM = require('react-dom')

var UserList = React.createClass({
    loadUsersFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadUsersFromServer();
        setInterval(this.loadUsersFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var userNodes = this.state.data.map(function(user){
                return <li> {user.first_name} </li>
            })
            console.log(userNodes)
        }
        return (
            <div>
                <h1>User List 3:</h1>
                <ul>
                    {userNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<UserList url='/api/users' pollInterval={1000} />, 
    document.getElementById('container'))