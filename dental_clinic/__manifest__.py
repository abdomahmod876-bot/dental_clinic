{
    "name" : "Dental Clinic Management",
    "version" : "19.0.0.1",
    "summary" : "Dental Clinic Management",
    "description" : "Dental Clinic Management",
    "category" : "Dental Clinic",
    "author" : "ENG_AbdElazim",
    "license" : "AGPL-3",
    "depends" : ["base", "mail", "web"],
    "data" : [ "security/security.xml","security/ir.model.access.csv","data/patient_sequence.xml", "views/patient_views.xml" ],
    "assets": {
        "web.assets_backend": [
            "dental_clinic/static/src/scss/dental.scss",
        ],
    },
    "installable" : True,
    "application" : True,
}
