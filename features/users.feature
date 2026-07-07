Feature: Gestion de usuarios

    Background:
        Given que realizo un login valido

    Scenario: Obtener usuarios

        When consulto la lista de usuarios

        Then la respuesta debe ser 200

        And la lista de usuarios no debe estar vacia

    Scenario: crear usuario usando tabla

        When creo un usuario con los siguientes datos 

            | name    | job       |
            | Brayann | Developer |

        Then la respuesta debe ser 201

        And el nombre debe ser "Brayann"

        And el trabajo debe ser "Developer"
