from pypureclient.flashblade import CertificatePatch

# change our built-in certificate named "global", which is used by the REST server and S3
# to a new certificate issued by my internal CA
cert_name = 'global'
cert_text = '-----BEGIN CERTIFICATE-----\nMIIESzCCAzOgAwIBAgIJAIJMKJXXDn/JMA0GCSqGSIb3DQEBBQUAMHYxCzAJBgNV\nBAYTAlVTMQ0wCwYDVQQIEwR0ZXN0MQ4wDAYDVQQHEwV0ZXN0IDENMAsGA1UEChME\ndGVzdDENMAsGA1UECxMEdGVzdDEVMBMGA1UEAxMMUHVyZSBTdG9yYWdlMRMwEQYJ\nKoZIhvcNAQkBFgR0ZXN0MB4XDTE3MTEwNjIyMzYyMFoXDTE4MTEwNjIyMzYyMFow\ndjELMAkGA1UEBhMCVVMxDTALBgNVBAgTBHRlc3QxDjAMBgNVBAcTBXRlc3QgMQ0w\nCwYDVQQKEwR0ZXN0MQ0wCwYDVQQLEwR0ZXN0MRUwEwYDVQQDEwxQdXJlIFN0b3Jh\nZ2UxEzARBgkqhkiG9w0BCQEWBHRlc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw\nggEKAoIBAQDcaGpPXJC1EC515wMEKyXEFuKFEDn4y1V5YmaLt+hXz8cfuA+gS3eD\nltP8PJah+7WrPouUQtfamHsuQtnFFLcVcdl83rIFX0m58zUiWbOUHI5wWnBYsqof\n52k/m40HM5XTATn5xpFsTSxm7vmlsKfGlQS7yI11HbD0OOz9CqT+iMFhTn/Wfyg2\nYOtmYIfCz0kt6wIFHlI9oPERwJ0JiMnPhsg0gerJwYl1j1vDhBiK32OVc4iIdOO4\nPVwpP1YbINr8LJ5qX2DOzBHDnaYrtJk9YEsSAwoqJ2/d29xA9JOeJwahl/M6aO48\nAbXbSlxVwOz0lEs85dseLp9dyTQb/uzjAgMBAAGjgdswgdgwHQYDVR0OBBYEFJJM\nML8khiOYzpaJP8sJCn0JSpx9MIGoBgNVHSMEgaAwgZ2AFJJMML8khiOYzpaJP8sJ\nCn0JSpx9oXqkeDB2MQswCQYDVQQGEwJVUzENMAsGA1UECBMEdGVzdDEOMAwGA1UE\nBxMFdGVzdCAxDTALBgNVBAoTBHRlc3QxDTALBgNVBAsTBHRlc3QxFTATBgNVBAMT\nDFB1cmUgU3RvcmFnZTETMBEGCSqGSIb3DQEJARYEdGVzdIIJAIJMKJXXDn/JMAwG\nA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBAKjQ/SFPra2YmtNynNukuHOl\nCryjsXjBkeiyyfg3Bt9+M+9F6Y4Sh3/SSJCb6LQaqTQkeJJeb1fOHNaFjAxkjvaI\n2tnlCwhpQuoSXNgQEMdidMi9+S8hBonlXYePYZUQbvAu1VAZrU6f0k2OEDcAPLvA\nhZLvrmZeug+VZp3JfVOdU+QnzUx2atBBfN5lMFFNdqOzZ5Yz/Ooi9CVA73szIevi\nE728OLimWQ91u1s16isjusK3+zoqirFC7PN6K63sp0gPAldgCQD2bywmwgaYDnzP\n+9ZWNy6ebn927Qh22YUPWhj+kiITkhxcVYPMx4QtRjJhs5pQVBqHOIDnJQJc7qY=\n-----END CERTIFICATE-----'
# use a private key that was encrypted with a passphrase
private_key = '-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,D6E1A92B08CB859F\n\nh+XvYwbbEIboztkR5/Gku7UsCnZtNI/ZYZru3jm/tRgjXR71PBgi9x1Rv5wyiDXA\n9F8xWyacRQgSqQCO2tc+rqoBTAd33wGo52k7BCuG2VJgbuzlZlC4vsyjKna1yGRw\nFHv+dHPWyTE/Cqcl0QQGjpqQmKbX6OXcUnDRp0IPzRf98A6DVZ/jbwuGl1JIkEme\nCuo4/5Hc4BMeHBYGtzbYZ83nFyrImhMQA+HzeULWSi0Ecx2vbafrlXVd0hI9E3c6\nsahuu6A9DSwEGWWW5x/ubq0i8mS94s7O4EjNoI8w6/yhd2edUTsTddJ2I+DJxOB1\nlBukWeph+/wAiCdVKuHW9A5xbPK0U24ipRh1vOG1ikeFR62gFktSnquOv4zpZL73\nSE7xWP1+FotaEgEL1hkHqfMfEnEL0/5oVyYVB9BZ2VaiystWvFk/mgLJiWGM0zx8\n5rA+0kqNTVYHhwElMUYMXILx3RMGVH+A0kKWvpl3BBuwDbQfgl0m1lLK6zZgtwVL\nkyctAjthTwC4KZorATa2CTBLq5cCSq1itoVueCYozuUPDMmCuC4Xf3dMEcYok+E5\nF4USqn7xcCqTu5ftqoiSt5bdJ7MOfL/KVXjQZAi/eUPaaREI27mqyfnVM6f2VcEp\nsQJnJg+zpcnBY0oICtGsakZWD0iE2ZA4FN177ogl8mlU4sY6XteHtPEFn8jjWuwW\ncylAo4jg/D6LPm+a7v1BYV41xLLQSFRvFGsyGON5CMg2vO9kjNnTDONNEchQ1C4A\nqIAIhjye+VD1F0L4McswRUQMISuWpbTND6HV2/DwXh9mDP2jVsttoJ3mjJrCeR1/\nTcMkN2C1isNUrRh+ReWtmanyhIorPLGX9TuDBef1r6caqVdGvDzjWaVUh6qTHsoY\nzt49SxXykIbZCdEbAQkoXfg8MuK+lxlGVEP/OS1uMXI8tVozBpepI8diFVznWpJo\nHVJCvcrOoIQr/B6kZX6mfqH5EJcnJPC4GUYwu+TRi03fmmKHi56xyWdrm/payoJH\n6ApOXeD4ViaFKkI6f69o5aADVZcmOWMqP6Yd8oxvl1Rn7ArR/RBcQwCMUZEA0dOs\ndu4S9hwTDlekT7unaVuXWmU9Js63DK82K3w+EjWUmYobX4tnM1nqJ4nBS8btt0kc\nBefHQP4gx72ytkJW4cVtFD/us0UBMTvODXDmBeZxlIJsNkU0EWyW+1kKBRpVhHGB\nofPRqYTk/m9yMzuDhutupW1uV+5g+lvpxXKQu4kSzJS6UVWZ33iz7yrvIOrJ3hxZ\nsJjWj+f0Bef/gym2JrGb1J756lPwBY4S/3/yiajbUvRvElOoVQB5XSH+th5N/hUJ\ntD2TJJsWnr/E6vwZjsYwK1hav/YcJi/YJdoXziZkKoYlf2WvwLAsvj9fNrpguwqV\npMJARiVwBDrWiB16GRdHxa0HwCJKB8Vpz9pDYQNdBseAhJzGmh5JaBiIbuVJaVwF\nZP+y2v/3Pa7wzAZTjD46V9EvADK6RW9If12OPHP4G2FvhdngxGbNjgZbEy0HUy4I\n6MRcPb3qaR5tnySoozrwW5IRYy7yZJ+UEg03nUi8eHKUL6anF5YzCg==\n-----END RSA PRIVATE KEY-----'
passphrase = 'example password'

create_body = CertificatePatch(certificate=cert_text, private_key=private_key, passphrase=passphrase)
res = client.patch_certificates(names=[cert_name], certificate=create_body)
print(res)
if type(res) == pypureclient.responses.ValidResponse:
    print(list(res.items))
# Other valid fields: ids
# See section "Common Fields" for examples