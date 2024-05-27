import python_jwt as jwt, jwcrypto.jwk as jwk, datetime

def verifyJWTToken(jwt_token): 
    '''
    Verify the JWT Token and return it.
    '''
    #Assuming we have the public key (as we do not have key details, hence adding a common public key for example)
    public_key = jwk.JWK.from_json('{"kty":"RSA","e":"AQAB","use":"sig","kid":"12345678","alg":"RS256","n":"nZtDdrzdqOE8uCka2xzMvrIvtSqBmWwF3472HOXQ8be0rOzgMN8z0stjA3r_pm7vSpyTkaajTu_ijWUOHQaqP0wJYE1179VRmhzCeAcWEgmb7oL4ZRTGaUJjHKMb6VEOLiv7EPOoEr8N8g72PQbhAHMwLI9UDG7b5JuGrh7pxRPbkt5ThDI97EUMVQ1esoh1VhzZGakSBbh4xpJAhn0nug9SNlE39rfBPtu4diEa3WFq70Pe9CXbwPl4qJkZA9avCLc2Qa2nbeWDgkx2ZpNv5jklOntOvfBvaUdEEWHCxWeZmJU3aMpdMOjtbAlpaIniQL4VqR73nME0veme78FBw"}')

    #Generally we get the private key in a secure way from betwork or safe storage, this demonstration is just for understanding.
    try:
        header, claims = jwt.verify_jwt(jwt_token, public_key, allowed_algs=['RS256'])
        if datetime.datetime.utcnow() > datetime.datetime.strptime(claims['exp'], "%Y-%m-%dT%H:%M:%S.%fZ"):
            raise jwt.JWTExpired("Token has expired")
        return claims
    except jwt.JWTExpired as e:
        raise jwt.JWTExpired("Token has expired")
    except jwt.JWTMissingKey as e:
        raise jwt.JWTMissingKey("Missing Key")
    except Exception as e:
        raise Exception("Failed to parse token")