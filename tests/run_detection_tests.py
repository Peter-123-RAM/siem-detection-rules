import json


def credential_stuffing(event):
    if event["EventID"] == 4625:
        if len(event["TargetUserName"]) > 10:
            return True
    return False


def web_shell(event):

    suspicious_parents = ["apache2", "nginx"]

    suspicious_children = [
        "/bin/bash",
        "/bin/sh"
    ]

    if event["ParentImage"] in suspicious_parents:
        if event["Image"] in suspicious_children:
            return True

    return False


def oauth_detection(event):

    risky_permissions = [
        "Mail.ReadWrite",
        "Files.ReadWrite",
        "offline_access"
    ]

    if event["OperationName"] == "Consent to application":
        if event["PermissionScope"] in risky_permissions:
            return True

    return False



print("SIEM Detection Validation Results")

print("------------------------------")


credential_tp = {
"EventID":4625,
"TargetUserName":[
"user1","user2","user3",
"user4","user5","user6",
"user7","user8","user9",
"user10","user11"
]
}


credential_fp = {
"EventID":4625,
"TargetUserName":[
"user1","user2"
]
}


print(
"Credential Stuffing TP:",
credential_stuffing(credential_tp)
)

print(
"Credential Stuffing FP:",
credential_stuffing(credential_fp)
)



web_tp = {

"ParentImage":"apache2",

"Image":"/bin/bash"

}


web_fp = {

"ParentImage":"apache2",

"Image":"php-fpm"

}


print(
"Web Shell TP:",
web_shell(web_tp)
)


print(
"Web Shell FP:",
web_shell(web_fp)
)



oauth_tp = {

"OperationName":
"Consent to application",

"PermissionScope":
"Mail.ReadWrite"

}


oauth_fp = {

"OperationName":
"Consent to application",

"PermissionScope":
"User.Read"

}


print(
"OAuth TP:",
oauth_detection(oauth_tp)
)


print(
"OAuth FP:",
oauth_detection(oauth_fp)
)
