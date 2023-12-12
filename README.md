# URL Shortner

https://url-shortner.io/


### Routes

- ``GET https://url-shortner.io/ RETURN HTML``

    Homepage

- ``GET https://url-shortner.io/admin RETURN HTML``
    
    Admin homepage

- ``POST https://url-shortner.io/ RETURN JSON``
    
    Shorten a url

- ``GET https://url-shortner.io/{key} RETURN REDIRECT``
    
    Go to a shortned URL

- ``GET https://url-shortner.io/admin/{secret_key} RETURN JSON``
    
    Get admin info for a URL

- ``DELETE https://url-shortner.io/admin/{secret_key} RETURN JSON``
    
    Delete a URL