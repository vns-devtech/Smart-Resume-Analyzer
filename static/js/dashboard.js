document.addEventListener("DOMContentLoaded", function () {

    const resumeScore = Number(
        document.getElementById("resumeChart").dataset.score
    );

    const atsScore = Number(
        document.getElementById("atsChart").dataset.score
    );

    new Chart(document.getElementById("resumeChart"), {

        type: "doughnut",

        data: {

            datasets: [{

                data: [resumeScore, 100 - resumeScore],

                backgroundColor: [

                    "#2563eb",

                    "#e5e7eb"

                ],

                borderWidth: 0

            }]

        },

        options: {

            cutout: "75%",

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

    new Chart(document.getElementById("atsChart"), {

        type: "doughnut",

        data: {

            datasets: [{

                data: [atsScore, 100 - atsScore],

                backgroundColor: [

                    "#10b981",

                    "#e5e7eb"

                ],

                borderWidth: 0

            }]

        },

        options: {

            cutout: "75%",

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

});