import React, { Component } from 'react'

export class header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm navbar-light bg-light">
        <a className="navbar-brand" href="#">Ambition</a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
            
            </ul>
            
        </div>
        </nav>
                )
            }
        }

export default header
