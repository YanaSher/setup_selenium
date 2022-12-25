pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'g++ main.ru -o simple-db'
            }
        }
        stage('test') {
            steps {
				sh """
				    PATH=$PATH:$WORKSPACE
				    python3 -m venv venv
				    . venv/bin/activate
				    pip3 install -r tests/requirements.txt
				    pytest -v tests -n${NUMBER} --url ${URL} --executor ${EXECUTOR} --browser ${BROWSER_NAME} --bv ${BROWSER_VERSION} --junitxml=report.xml
                """
            }
        }
        stage('report-xml') {
            steps {
                junit 'report.xml'
            }
        }
        stage('report-allure') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}
Footer
