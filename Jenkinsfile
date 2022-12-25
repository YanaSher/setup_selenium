pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }
        stage('test') {
            steps {
				sh './venv/lib/python3.8/site-packages/pytest -v tests -n${NUMBER} --url ${URL} --executor ${EXECUTOR} --browser ${BROWSER_NAME} --bv ${BROWSER_VERSION} --junitxml=report.xml'

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
