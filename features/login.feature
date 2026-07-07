Feature: Login

    Como usuario 
    puedo autenticarme 
    Para obtener un token

    Scenario: Login exitoso

        When realizo login con email "eve.holt@reqres.in" y password "cityslicka"

        Then la respuesta deber ser 200

        And debe existir un token

    Scenario Outline: Validar distintos logins

        When realizo login con email "<email>" y password "<password>"

        Then la respuesta deber ser <status>

    Examples:
        |email                |password      |status |
        |eve.holt@reqres.in   |cityslicka    |200    |
        |eve.holt@reqres.in   |incorrecto    |400    |
        |login@reqres.in      |              |400    |

