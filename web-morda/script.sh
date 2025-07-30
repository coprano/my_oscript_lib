#!/bin/bash
set -eou pipefail
# ====== CONFIG ======
IMAGE_NAME="web-morda-rac-panel"
IMAGE_TAG="latest"
ARCHIVE_NAME="docker_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
BUILD_CONTEXT="."  # Set to where your Dockerfile is
DOCKER_COMPOSE_FILE="docker-compose.yml"
ENV_FILE=".env"  # optional

# ====== BUILDx SETUP ======
echo "🔧 Setting up buildx..."
docker buildx create --use --name amd64-builder 2>/dev/null || docker buildx use amd64-builder

# ====== BUILD IMAGE ======
echo "🐳 Building Docker image for linux/amd64/v4..."
docker buildx build \
  --platform linux/amd64 \
  --output type=docker \
  -t ${IMAGE_NAME}:${IMAGE_TAG} \
  ${BUILD_CONTEXT}

# ====== SAVE IMAGE TO TARBALL ======
IMAGE_TAR="${IMAGE_NAME}_${IMAGE_TAG}_amd64.tar"
echo "💾 Saving Docker image to ${IMAGE_TAR}..."
docker save ${IMAGE_NAME}:${IMAGE_TAG} -o ${IMAGE_TAR}

# ====== CREATE ARCHIVE ======
echo "📦 Creating backup archive ${ARCHIVE_NAME}..."
FILES_TO_ARCHIVE=("${IMAGE_TAR}" "${DOCKER_COMPOSE_FILE}")
[ -f "${ENV_FILE}" ] && FILES_TO_ARCHIVE+=("${ENV_FILE}")

tar -czvf "${ARCHIVE_NAME}" "${FILES_TO_ARCHIVE[@]}"

# ====== CLEANUP IMAGE TARBALL ======
echo "🧹 Cleaning up temporary image file..."
rm -f "${IMAGE_TAR}"

echo "✅ Archive ready: ${ARCHIVE_NAME}"
