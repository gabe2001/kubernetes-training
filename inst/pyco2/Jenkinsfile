node {
	stage('Checkout') {
		checkout scm
	}
	stage('Build Container') {
		docker.build('pamvdam/pyco2', '-f Dockerfile .')
	}

	stage('Write properties') {
	    sh "> spinnaker.properties"
	    sh "echo 'JOB_NAME=${JOB_NAME}' >> spinnaker.properties"
	    sh "echo 'BUILD_ID=${BUILD_ID}' >> spinnaker.properties"
	    archiveArtifacts artifacts: 'spinnaker.properties', fingerprint: true
	}
	stage('Push to DockerHub') {
		docker.withRegistry('', 'dockerhubCredential') {
			docker.image('pamvdam/pyco2').push('${BUILD_ID}')
	   }
	}
}
