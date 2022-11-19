import '../stylings/newSearch.css'

function Reactive(){
    return(
        <Card
        title="CMPT370"
        body="my fav class"
        pre="CMPT280"
        dep="None" />

    )
}

function Card(props){
    return(
        <div className="card">
            <t className="card__title">{props.title}</t>
            <b className="card__body">{props.body}</b>
            <p className="card__pre">{props.pre}</p>
            <d className="card__dep">{props.dep}</d>
        </div>
            
    )
}

//export default Reactive;
export default Reactive