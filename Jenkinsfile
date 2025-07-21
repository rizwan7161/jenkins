node {
    stage('Pull Code') {
        git 'https://github.com/rizwan7161/jenkins.git'
    }

    stage('Build') {
        sh 'docker-compose build'
    }

    stage('Start DB and Backend') {
        sh 'docker-compose up -d db backend'
        sh 'sleep 10'
    }

    stage('Migration') {
        sh 'docker-compose exec backend alembic upgrade head'
    }

    stage('Test') {
        sh 'curl --fail http://localhost:8000/docs || exit 1'
    }

    stage('Deploy') {
        sh 'docker-compose up -d'
    }
}
